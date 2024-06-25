function agregarAuto(id, nombre, precio) {
  console.log('agregarAuto')
  let carrito = JSON.parse(localStorage.getItem('carrito'));
  if(!carrito){
    carrito = [];
  }
  carrito.push({id, nombre, precio});
  localStorage.setItem('carrito', JSON.stringify(carrito));
  MostrarCarrito()
  }

function MostrarCarrito(){
  let carrito = JSON.parse(localStorage.getItem('carrito'));
  if(!carrito){
    carrito = [];
  }
  let listaCarrito = document.getElementById('CarritoDeCompra');
  let total = 0
  listaCarrito.innerHTML = ''
  for (let i = 0; i < carrito.length; i++) {
    let autoli = document.createElement('li')
    autoli.textContent = `${carrito[i].nombre} - $${carrito[i].precio}`;
    listaCarrito.appendChild(autoli);
    total = total + Number(carrito[i].precio)
  }
  document.getElementById('total').textContent = total
}

function eliminarTodo() {
  localStorage.removeItem('carrito');
  MostrarCarrito();
}