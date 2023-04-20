var est = []; //Lista de estudiantes
var grup = []; //lista de grupos
var sem = []; //listas de semanas
var day = []; //listas de dias
var bloq = []; // listas de bloques
var cumpli = []; //lista de cumplimiento
var coment = []; //lista de comentarios
var lecture = [];
var a_j = [];



function agregarOH() {
        event.preventDefault(); // Evita que el formulario se envíe

        // Obtén los valores seleccionados del select y el input

        var grupo = document.getElementById('grupo').value;
        var estudiante = document.getElementById('seleccion-estudiantes').value;
        var semana = document.getElementById('Semana').value;
        var dia = document.getElementById('Dsemana').value;
        var bloque = document.getElementById('Bloque').value;
        var cumplimiento = document.getElementById('Cumplimiento').value;
        var comentario = document.getElementById('Comentario').value;



        // Crea un nuevo elemento de lista y añade los valores a la lista
        var nuevoElemento = document.createElement('li');
        nuevoElemento.textContent = `Grupo: ${grupo}, Estudiante: ${estudiante}, Semana: ${semana},
        Dia: ${dia}, Bloque: ${bloque}, Cumplimiento: ${cumplimiento}, Comentario: ${comentario}`
        document.getElementById('listaEstudiantes').appendChild(nuevoElemento);


        est.push(estudiante);
        grup.push(grupo);
        sem.push(semana);
        day.push(dia);
        bloq.push(bloque);
        cumpli.push(cumplimiento);
        coment.push(comentario);


        //document.getElementById('grupo').value = '';
        document.getElementById('seleccion-estudiantes').value = '';
}

function enviarOH(){
    event.preventDefault(); // Evita que el formulario se envíe
     let url = "/procesarOH";
     var data = JSON.stringify({"estudiantes": est , "grupos": grup, "semana" : sem, "dia": day, "bloque": bloq, "cumplimiento": cumpli, "comentario": coment });
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

    alert(`Datos enviados exitosamente, se enviarion ${est.length} estudiantes`);
    location.reload();
}


function agregarClass() {
        event.preventDefault(); // Evita que el formulario se envíe
        //Grupo, Nombre, Lecture, A_J, Comentario
        // Obtén los valores seleccionados del select y el input

        var grupo = document.getElementById('grupo').value;
        var estudiante = document.getElementById('seleccion-estudiantes').value;
        var clase = document.getElementById('nClass').value;
        var accion = document.getElementById('a_j').value;
        var comentario = document.getElementById('Comentario').value;

        var nuevoElemento = document.createElement('li');
        nuevoElemento.textContent = `Grupo: ${grupo}, Estudiante: ${estudiante}, Clase: ${clase},
         [A]/[J]: ${accion},Comentario: ${comentario}`
        document.getElementById('listaEstudiantes').appendChild(nuevoElemento);

        grup.push(grupo);
        est.push(estudiante);
        lecture.push(clase);
        a_j.push(accion)
        coment.push(comentario);

        //document.getElementById('grupo').value = '';
        document.getElementById('seleccion-estudiantes').value = '';
}

function enviarClass(){
    event.preventDefault();
     let url = "/procesarClass";
     var data = JSON.stringify({"estudiantes": est , "grupos": grup, "semana" : sem, "dia": day, "bloque": bloq, "cumplimiento": cumpli, "comentario": coment });
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

    alert(`Datos enviados exitosamente, se enviarion ${est.length} estudiantes`);
    location.reload();
}