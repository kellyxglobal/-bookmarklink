template = {
    "swagger": "2.0",
    "info": {
        "title": "Book Your Link - API",
        "description": "API for bookmarking links or url shortening",
        "contact": {
            "responsibleOrganization": "KellyX Global Web Solutons Agency",
            "responsibleDeveloper": "Kelechi Anyaegbu",
            "email": "kellyxglobal@gmail.com",
            "url": "https://twitter.com/kellyxglobal",
        },
        "termsOfService": "https://twitter.com/kellyxglobal",
        "version": "1.0"
    },
    "basePath": "/api/v1",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json', 
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}