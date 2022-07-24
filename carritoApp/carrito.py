class Carrito():
    def __init__(self, request):
        self.request=request # almacena la peticion
        self.session=request.session # inicia la sesion
        carrito=self.session.get("carrito") # carrito de la compra para cada sesion
        
        if not carrito:
            carrito=self.session["carrito"]={}
        else:
            self.carrito=carrito
            
    def agregar_producto(self, producto):
        if (str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id]={
                "producto_id":producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1 #si el producto ya esta en el carrito, incrementa el value "cantidad" en 1
                    break
                
        self.guardar_carrito()
        
    def guardar_carrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True
        
    def eliminar_producto(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()
            
    def restar_unidades(self, producto):
        for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar_producto(producto)
                    break
        self.guardar_carrito
        
    def limpiar_carrito(self):
        self.session["carrito"]={}
        self.session.modified=True