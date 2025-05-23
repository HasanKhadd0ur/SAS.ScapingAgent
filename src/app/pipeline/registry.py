from app.core.ml.sentiment_analysis_model import SentimentAnalysisModel
from app.pipeline.pipeline import Pipeline
from app.pipeline.stages.hate_speach_filtering_stage import HateSpeachFilteringStage
from app.pipeline.stages.master_notifying_stage import MasterNotifyingStage
from app.pipeline.stages.messages_publishing_stage import MessagesPublishingStage
from app.pipeline.stages.keyword_filter_stage import KeywordFilterStage
from app.pipeline.stages.normalize_text_stage import NormalizeTextStage
from app.pipeline.stages.messages_saving_stage import MessagesSavingStage
from app.pipeline.stages.sentiment_analysis_stage import SentimentAnalysisStage

# The filter registry stores the filter instances
PIPELINE_REGISTRY = {
    "keyword_filter_stage": KeywordFilterStage,
    "normalize_stage": NormalizeTextStage,
    "messages_publishing_stage": MessagesPublishingStage
}

# The order in which filters are applied
PIPELINE_ORDER = [
    "keyword_filter_stage",
    "normalize_stage",
]

# Define the sentiment analysis model 
SAModel =SentimentAnalysisModel()

# Define a preprocessing pipelie
preprocessing_pipeline= Pipeline()
preprocessing_pipeline.add_filter(NormalizeTextStage)
preprocessing_pipeline.add_filter(SentimentAnalysisStage,SAModel)
preprocessing_pipeline.add_filter(HateSpeachFilteringStage)

# Define a publishing pipeline
publishing_pipeline= Pipeline()
publishing_pipeline.add_filter(MessagesPublishingStage)
publishing_pipeline.add_filter(MessagesSavingStage)
publishing_pipeline.add_filter(MasterNotifyingStage)

