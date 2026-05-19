
import os

# Base Project Path
BASE_PATH = "/content/drive/MyDrive/smartpdf_insight_engine"

# Data Paths
UPLOAD_FOLDER = os.path.join(BASE_PATH, "data/uploads")
PROCESSED_FOLDER = os.path.join(BASE_PATH, "data/processed")

# Database Path
DATABASE_PATH = os.path.join(BASE_PATH, "database/chunks.db")

# PDF Constraints
MAX_FILE_SIZE_MB = 5
MAX_PAGES = 20
MAX_WORDS = 12000

# Chunking Settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Supported File Types
SUPPORTED_EXTENSIONS = [".pdf"]

# Allowed PDF Type
ALLOWED_PDF_TYPE = "digital_only"
