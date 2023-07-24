"""List of all data sources supported by Docq."""

from enum import Enum

from .aws_s3 import AwsS3
from .azure_blob import AzureBlob
from .knowledge_base_scraper import KnowledgeBaseScraper
from .manual_upload import ManualUpload
from .web_scraper import WebScraper


class SpaceDataSources(Enum):
    """Space datasource list."""

    MANUAL_UPLOAD = ManualUpload()
    AZURE_BLOB = AzureBlob()
    AWS_S3 = AwsS3()
    WEB_SCRAPER = WebScraper()
    KNOWLEDGE_BASE_SCRAPER = KnowledgeBaseScraper()