


<script lang="ts" setup>



</script>
<template>
  <div class="flex flex-col min-h-screen">
    <div class="flex-grow flex flex-col justify-center items-center  text-2xl">
      <h1 class="font-bold">
        Bienvenido!
      </h1>
      <h2 class="text-center mt-4 ">
        Este proyecto consiste en un Reproductor de video, con balanceo de cargas en un servidor hecho en python y
        Nginx.

      </h2>

      <h3>
        <a href="https://github.com/AntJimenezZ/ProyectoSO" target="_blank" class="hover:underline text-blue-900">Link al repositorio de github</a>
      </h3>
      <div class=" mt-32">
          <UButton block label="INICIAR" color="fuchsia" size="xl" padded to="/test"/>
    </div>
  </div>

  <footer class="bg-gray-800 text-white py-4">
    <div class="container mx-auto flex justify-around">
      <div class="text-center">
        <a href="https://github.com/AntJimenezZ" target="_blank" class="hover:underline">
          <img src="https://github.com/AntJimenezZ.png" alt="Anthony Jiménez" class="w-16 h-16 rounded-full mx-auto">
          <p>Anthony Jiménez</p>
        </a>
      </div>
      <div class="text-center">
        <a href="https://github.com/fabian-rojasu" target=" _blank" class="hover:underline">
          <img src="https://github.com/fabian-rojasu.png" alt="Fabián Rojas" class="w-16 h-16 rounded-full mx-auto">
          <p>Fabián Rojas</p>
        </a>
      </div>
      <div class="text-center">
        <a href="https://github.com/KevinVarelaR" target="_blank" class="hover:underline">
          <img src="https://github.com/KevinVarelaR.png" alt="Kevin Varela" class="w-16 h-16 rounded-full mx-auto">
          <p>Kevin Varela</p>
        </a>
      </div>
    </div>
  </footer>
  </div>
</template>
