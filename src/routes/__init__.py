def routes(app):
    from .home import home
    from .auth import auth
    from .user import user
    from .allcodes import allcodes
    from .product import product
    from .detail_product import detail_product
    from .order import order
    from .line_item import line_item
    from .option import option

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(allcodes, url_prefix="/allcodes")
    app.register_blueprint(product, url_prefix="/product")
    app.register_blueprint(detail_product, url_prefix="/detail_product")
    app.register_blueprint(order, url_prefix="/order")
    app.register_blueprint(line_item, url_prefix="/line-item")
    app.register_blueprint(option, url_prefix="/option")
