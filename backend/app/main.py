"""
main.py

Enterprise Healthcare Digital Twin Platform

Features
--------
✓ FastAPI
✓ Loguru Logging
✓ Startup / Shutdown
✓ Exception Handling
✓ CORS
✓ Health Check
✓ Router Registration
"""

from contextlib import asynccontextmanager
import sys
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config.settings import settings
logger = settings.get_logger()


from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.routers.digital_twin_router import router as digital_twin_router
from app.routers.ui_router import router as ui_router
from fastapi.routing import APIRoute

from app.database.mysql_db import MySQLDBManager
from app.database.chroma_db import ChromaDBManager

#from app.config.llm_config import MYSQL_CONNECTION_STRING,CHROMA_DIRECTORY,CHROMA_COLLECTION,EMBEDDING_MODEL

# ==========================================================
# Configure Loguru
# ==========================================================

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:"
        "<cyan>{function}</cyan>:"
        "<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    ),
)

logger.add(
    "logs/digital_twin.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
    level="DEBUG",
)


# ==========================================================
# Lifespan
# ==========================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("=" * 80)
    logger.info("Starting Healthcare Digital Twin Platform")
    logger.info("=" * 80)

    try:

        # --------------------------------------------------
        # MySQL
        # --------------------------------------------------

        mysql = MySQLDBManager(
            connection_string=settings.MYSQL_CONNECTION_STRING
        )

        if mysql.health_check():

            logger.success("MySQL Connected")

        else:

            logger.error("Unable to connect to MySQL")

        app.state.mysql = mysql

        # --------------------------------------------------
        # Chroma
        # --------------------------------------------------

        chroma = ChromaDBManager(
            persist_directory=settings.CHROMA_DIRECTORY,
            collection_name=settings.CHROMA_COLLECTION,
            embedding_model=settings.embedding_model,
        )

        if chroma.health_check():

            logger.success("Chroma Connected")

        else:

            logger.error("Unable to connect to Chroma")

        app.state.chroma = chroma

        logger.success("Application Started")

        yield

    finally:

        logger.info("Stopping Application")

        try:

            app.state.mysql.close()

        except Exception:

            pass

        logger.success("Shutdown Completed")


# ==========================================================
# FastAPI
# ==========================================================

app = FastAPI(
    title="Healthcare Digital Twin Platform",
    description="Enterprise Agentic AI Healthcare Platform",
    version="1.0.0",
    lifespan=lifespan,
)


# ==========================================================
# Middleware
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# Request Logging
# ==========================================================

@app.middleware("http")
async def log_requests(
    request: Request,
    call_next,
):

    start = time.time()

    logger.info(
        "{} {}",
        request.method,
        request.url.path,
    )

    response = await call_next(request)

    elapsed = round(
        time.time() - start,
        3,
    )

    logger.info(
        "{} completed in {} sec",
        request.url.path,
        elapsed,
    )

    return response


# ==========================================================
# Global Exception
# ==========================================================

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception,
):

    logger.exception(exc)

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": str(exc),
        },
    )


# ==========================================================
# Root
# ==========================================================

@app.get("/")
async def root():

    return {
        "application": "Healthcare Digital Twin Platform",
        "version": "1.0.0",
        "status": "Running",
    }


# ==========================================================
# Router
# ==========================================================

app.include_router(digital_twin_router)

BASE_DIR = Path(__file__).resolve().parent

# Static Files
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)

# HTMX Pages
app.include_router(ui_router)

print("=" * 80)
print("ALL ROUTES")
print("=" * 80)

for route in app.routes:
    print(type(route).__name__, getattr(route, "path", "NO PATH"))

print("=" * 80)
print("API ROUTES")
print("=" * 80)

for route in app.routes:
    if isinstance(route, APIRoute):
        print(
            route.path,
            route.methods,
            route.name,
        )

print("UI Router :", ui_router)
print("API Router:", digital_twin_router)
