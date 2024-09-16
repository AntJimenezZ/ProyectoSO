<script lang="ts" setup>
const cargarCancion = () => {
  console.log('Cargando canción...');
  const video = document.querySelector('video');
  video.play();
}
</script>

<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <video class="border-2 border-gray-500 w-full max-w-6xl" controls>
      <source src="http://localhost:8080/song" type="video/mp4">
      Tu navegador no soporta la etiqueta de video.
    </video>
  </div>
</template>

<style scoped>
/* Puedes agregar estilos aquí si es necesario */
</style>