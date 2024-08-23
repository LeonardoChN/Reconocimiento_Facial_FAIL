<h3>Reconocimiento facial con django y modulo Face_recognition</h3>	


Debemos installar las siguientes librerias
comando en powershell

"pip install" 

<ol>
  <li>Numpy</li>
  <li>Pillow</li>
  <li>django face_recognition opencv-python numpy pillow</li>
  <li>face_recognition</li>
  <li>dlib</li>
  <li>cmake</li>
  <li>opencv-python</li>
</ol>

<h3> para comprobar que se instalo bien ejecutamos en shell, python y ejecutamos el siguiente codigo </h3>

import face_recognition
print(face_recognition)

<h3> luego de instalar el dlib, verificamos en el path de python </h3>
import dlib
print(dlib.__version__)

<br>

<h2> problemas con la instalacion dlib </h2>

<ol>
    <li>Microsoft visual c++ x64: https://aka.ms/vs/17/release/vc_redist.x64.exe </li>
    <li>Microsoft C++ Build Tools:  https://visualstudio.microsoft.com/es/visual-cpp-build-tools/</li>
    <li>DLIB:  https://github.com/z-mahmud22/Dlib_Windows_Python3.x/tree/main   (Descarga segun tu version de Python) </li>
    <li>face_recognition_models:  https://github.com/ageitgey/face_recognition_models</li>
    <li>CMAKE:   https://cmake.org/download/</li>
</ol>




**NOTA** Me dio muchos ERRORES HACERLO CON Face_cognition debido a que no me reconocio la libreria, es decir lo instale e instala correctamente, me da la version y al momento de realizar el ***pip list*** me lo toma y me lo muestra en el listado, 
pero al momento de ejecutar el servidor djagno me pide que instale la libreria desde git *(tal cual lo puse en el listado)* 

es por eso que lo realizare nuevamente en otro repositorio con **OpenCV y FaceNet**

Adios!.

![Goku GIF](https://media.giphy.com/media/1J2FKJ31JKn4I/giphy.gif)

[Ver en GIPHY](https://giphy.com/gifs/goku-1J2FKJ31JKn4I)
