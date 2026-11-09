"""
database/mysql_db.py

Enterprise MySQL Database Manager

Features
--------
- SQLAlchemy 2.x
- Connection Pooling
- Session Management
- Transaction Handling
- Health Check
- CRUD Operations
- Loguru Logging
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Dict, List, Optional

from app.config.settings import settings
logger = settings.get_logger()

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker


class MySQLDBManager:
    """
    Enterprise MySQL Database Manager
    """

    def __init__(
        self,
        connection_string: str,
        pool_size: int = 10,
        max_overflow: int = 20,
        pool_recycle: int = 1800,
        echo: bool = False,
    ) -> None:

        logger.info("Initializing MySQL Database Manager")

        self.connection_string = connection_string

        try:

            self.engine = create_engine(
                connection_string,
                pool_size=pool_size,
                max_overflow=max_overflow,
                pool_recycle=pool_recycle,
                pool_pre_ping=True,
                future=True,
                echo=echo,
            )

            self.SessionLocal = sessionmaker(
                bind=self.engine,
                autoflush=False,
                autocommit=False,
                future=True,
            )

            logger.success("MySQL Engine Created Successfully")

        except Exception as ex:

            logger.exception(ex)
            raise

    # ==========================================================
    # Session
    # ==========================================================

    @contextmanager
    def get_session(self):

        session = self.SessionLocal()

        try:

            logger.debug("Opening database session")

            yield session

            session.commit()

            logger.debug("Transaction committed")

        except Exception as ex:

            logger.exception(ex)

            session.rollback()

            logger.warning("Transaction rolled back")

            raise

        finally:

            session.close()

            logger.debug("Database session closed")

    # ==========================================================
    # Execute Query
    # ==========================================================

    def execute_query(
        self,
        query: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:

        logger.info("Executing Query")

        logger.debug(query)

        with self.get_session() as session:

            result = session.execute(
                text(query),
                params or {},
            )

            rows = result.mappings().all()

            logger.success(
                "{} rows returned",
                len(rows),
            )

            return [dict(row) for row in rows]

    # ==========================================================
    # Execute Non-Query
    # ==========================================================

    def execute_non_query(
        self,
        query: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> int:

        logger.info("Executing Update")

        with self.get_session() as session:

            result = session.execute(
                text(query),
                params or {},
            )

            affected = result.rowcount

            logger.success(
                "{} rows affected",
                affected,
            )

            return affected

    # ==========================================================
    # Insert
    # ==========================================================

    def insert(
        self,
        query: str,
        params: Dict[str, Any],
    ) -> int:

        logger.info("Insert Operation")

        return self.execute_non_query(
            query,
            params,
        )

    # ==========================================================
    # Update
    # ==========================================================

    def update(
        self,
        query: str,
        params: Dict[str, Any],
    ) -> int:

        logger.info("Update Operation")

        return self.execute_non_query(
            query,
            params,
        )

    # ==========================================================
    # Delete
    # ==========================================================

    def delete(
        self,
        query: str,
        params: Dict[str, Any],
    ) -> int:

        logger.info("Delete Operation")

        return self.execute_non_query(
            query,
            params,
        )

    # ==========================================================
    # Fetch One
    # ==========================================================

    def fetch_one(
        self,
        query: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:

        logger.info("Fetching One Record")

        with self.get_session() as session:

            result = session.execute(
                text(query),
                params or {},
            )

            row = result.mappings().first()

            if row:

                logger.success("Record Found")

                return dict(row)

            logger.warning("No Record Found")

            return None

    # ==========================================================
    # Health Check
    # ==========================================================

    def health_check(self) -> bool:

        logger.info("Running Database Health Check")

        try:

            with self.get_session() as session:

                session.execute(text("SELECT 1"))

            logger.success("Database Connection Successful")

            return True

        except SQLAlchemyError as ex:

            logger.exception(ex)

            return False

        except Exception as ex:

            logger.exception(ex)

            return False

    # ==========================================================
    # Table Exists
    # ==========================================================

    def table_exists(
        self,
        table_name: str,
    ) -> bool:

        logger.info(
            "Checking Table '{}'",
            table_name,
        )

        query = """
        SELECT COUNT(*) AS total
        FROM information_schema.tables
        WHERE table_schema = DATABASE()
        AND table_name = :table_name
        """

        result = self.fetch_one(
            query,
            {
                "table_name": table_name
            },
        )

        return result["total"] > 0

    # ==========================================================
    # Database Info
    # ==========================================================

    def database_info(self) -> Dict[str, Any]:

        logger.info("Getting Database Information")

        version = self.fetch_one(
            "SELECT VERSION() AS version"
        )

        database = self.fetch_one(
            "SELECT DATABASE() AS database_name"
        )

        return {
            "database": database["database_name"],
            "version": version["version"],
        }

    # ==========================================================
    # Close Engine
    # ==========================================================

    def close(self):

        logger.info("Disposing SQLAlchemy Engine")

        self.engine.dispose()

        logger.success("Database Engine Closed")