var est = [];
var grup = [];

function agregar() {
        event.preventDefault(); // Evita que el formulario se envíe

        // Obtén los valores seleccionados del select y el input
        var grupo = document.getElementById('grupo').value;
        var estudiante = document.getElementById('seleccion-estudiantes').value;

        // Crea un nuevo elemento de lista y añade los valores a la lista
        var nuevoElemento = document.createElement('li');
        nuevoElemento.textContent = 'Grupo: ' + grupo + ', Estudiante: ' + estudiante;
        document.getElementById('listaEstudiantes').appendChild(nuevoElemento);
        est.push(estudiante)
        grup.push(grupo)


        //document.getElementById('grupo').value = '';
        document.getElementById('seleccion-estudiantes').value = '';
}

function enviar(){
    event.preventDefault(); // Evita que el formulario se envíe
     let url = "/procesar";
     var data = JSON.stringify({"estudiantes": est , "grupos": grup});
    let http = new XMLHttpRequest();
    http.open("POST", url);
    http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    http.send(data);

    http.onreadystatechange = function () {
        if (http.readyState === XMLHttpRequest.DONE) {
            if (http.status !== 200) {
                // Manejar la respuesta del servidor
                 console.error("Error en la solicitud:", http.statusText);
            }
        }
    };

     // http.send()

}

