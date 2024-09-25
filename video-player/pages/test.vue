<script lang="ts" setup>
import { ref } from 'vue';	

const getAllVideos = async () => {
  try {
    const response = await fetch('http://localhost:80/allVideos');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

const getAllSongs = async () => {
  try {
    const response = await fetch('http://localhost:8080/allSongs');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  getAllVideos();
});

const items = [{
  label: 'Videos',
  icon: 'i-heroicons-video-camera'
}, {
  label: 'Canciones',
  icon: 'i-heroicons-musical-note'
}];

const isOpen = ref(false);
const selectedMedia = ref('');

const toggleDropdown = () => {
  isOpen.value = !isOpen.value;
};

const mediaOptions = ref([
  { label: 'Videos', value: 'videos' },
  { label: 'Canciones', value: 'canciones' }
]);

const selectMedia = (option: string) => {
  selectedMedia.value = option;
};
</script>

<style scoped>
.selected-option {
  background-color: #d3d3d3; 
}
.container {
  display: flex;
  align-items: flex-start;
  justify-content: flex-end; 
}
.select-container {
  margin-left: 16px; 
  margin-right: 16px; 
}
.custom-select {
  width: 300px; 
}
</style>

<template>
  <div class="container mt-4">
    <div class="relative inline-block select-container">
      <button @click="toggleDropdown" class="custom-select p-2 bg-gray-200 rounded">
        Select an option ▼
      </button>
      <ul v-if="isOpen" class="absolute w-full bg-white border mt-2 rounded z-10">
        <li 
          v-for="option in mediaOptions" 
          :key="option.value" 
          @click="selectMedia(option.label)" 
          :class="{'selected-option': selectedMedia === option.label}"
          class="p-2 hover:bg-gray-100 cursor-pointer">
          {{ option.label }}
        </li>
      </ul>
    </div>
    <div class="flex-grow flex justify-center">
      <UTabs :items="items" class="w-full max-w-6xl" style="min-height: 400px;">
        <template #item="{ item }">
          <div class="flex justify-center items-center w-full h-full">
            <!-- Videos -->
            <div v-if="item.label === 'Videos'">
              <video class="border-2 border-gray-500 w-full" controls>
                <source src="http://localhost:80/sendVideo?name=DJ MADNESS X MOB - Fess ka fe bang (acetone riddim)" type="video/mp4">
                Your browser does not support the video tag.
              </video>
            </div>
            <!-- Canciones -->
            <div v-if="item.label === 'Canciones'" class="w-full mt-40">
              <audio class="border-2 border-gray-500 w-full" controls>
                <source src="http://localhost:80/sendVideo" type="audio/mp3">
                Your browser does not support the audio tag.
              </audio>
            </div>
          </div>
        </template>
      </UTabs>
    </div>
  </div>
</template>
