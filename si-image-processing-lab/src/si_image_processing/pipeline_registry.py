from si_image_processing.pipelines.image_processing import pipeline as ip

def register_pipelines():
    return {
        "__default__": ip.create_pipeline()
    }