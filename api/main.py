from groa_ds_api import create_app
import uvicorn

application = app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level='info')
