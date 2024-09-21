<script lang="ts" setup>


const getAllVideos = async () => {
  try {
    const response = await fetch('http://localhost:8080/allVideos');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

const gellAllSongs = async () => {
  try {
    const response = await fetch('http://localhost:8080/allSongs');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

const items = [{
  label: 'Videos',
  icon: 'i-heroicons-video-camera'
}, {
  label: 'Canciones',
  icon: 'i-heroicons-musical-note'
}];


</script>

<template>
  <div class="flex justify-center items-center mt-10">
    <UTabs :items="items" class="w-full max-w-6xl" style="min-height: 400px;">
      <template #item="{ item }">

        <div class="flex justify-center items-center w-full h-full">
          <!-- Videos -->
          <div v-if="item.label === 'Videos'">
            <video class="border-2 border-gray-500 w-full" controls>
              <source src="http://localhost:8080/sendVideo" type="video/mp4">
              Tu navegador no soporta la etiqueta de video.
            </video>
          </div>

          <!-- Canciones -->
          <div v-if="item.label === 'Canciones'" class="w-full mt-40">
            <audio class="border-2 border-gray-500 w-full" controls>
              <source src="http://localhost:8080/sendVideo" type="audio/mp3">
              Tu navegador no soporta la etiqueta de audio.
            </audio>
          </div>
        </div>
      </template>
    </UTabs>
  </div>
</template>

 
