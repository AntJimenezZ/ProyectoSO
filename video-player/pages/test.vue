<script lang="ts" setup>


const people = ref<Media[]>([]);

const getAllVideos = async () => {
  try {
    const response = await fetch('http://localhost:80/allVideos');
    const data = await response.json();
    console.log(data);

    let id = 0;
    people.value = data.map((label: string) => ({ id: id++, label })); 

    console.log("People data:", people.value);
  } catch (error) {
    console.error(error);
  }
};

const testing = () => {
  console.log("Selected:", selected.value);
};


onBeforeMount(async () => {
  await getAllVideos();
});

const items = [{
  label: 'Videos',
  icon: 'i-heroicons-video-camera'
}, {
  label: 'Canciones',
  icon: 'i-heroicons-musical-note'
}];

interface Media {
  id: number;
  label: string;
}

const selected = ref<Media[]>([people.value[0]]); 
const videoSrc = ref<string>('');
const selectedMediaUrl = ref<string>('');
const selectedMedia = ref<string>('');

const handleSelectionChange = async (newSelection: Media[]) => {

  //@ts-ignore
  const song: String = newSelection.label;
  
  console.log("SOOOOONG ",song)
  const encodedMediaName = encodeURIComponent(`${song}`);
  console.log("como se vería lo que está adentor del fehct", `http://localhost:80/sendVideo?name=${encodedMediaName}`);
  try {
    const response = await fetch(`http://localhost:80/sendVideo?name=${encodedMediaName}`);
    const data = await response.blob();
    selectedMediaUrl.value = URL.createObjectURL(data); // Crear una URL temporal para el archivo

    console.log("pene vs vagina 2", selectedMediaUrl.value)
  } catch (error) {
    console.error('Error al cargar el video:', error);
  }
};


watch(selected, (newSelection) => {
  handleSelectionChange(newSelection);
});





</script>

<template>
  <div class="container mt-4">
    <div class="relative inline-block select-container">
      <UCommandPalette v-model="selected" nullable :autoselect="false" :groups="[{ key: 'people', commands: people }]"
        :fuse="{ resultLimit: 6, fuseOptions: { threshold: 0.1 } }" class="w-72 h-96" />
    </div>
    <div class="flex-grow flex justify-center">
      <UTabs :items="items" class="w-full max-w-6xl" style="min-height: 400px;">
        <template #item="{ item }">
          <div class="flex justify-center items-center w-full h-full">
            <!-- Videos -->
            <div v-if="item.label === 'Videos'">
              <video :key="selectedMediaUrl" class="border-2 border-gray-500 w-full" controls>
                <source :src="selectedMediaUrl" type="video/mp4">
                Your browser does not support the video tag.
              </video>
            </div>
            <!-- Canciones -->
            <div v-if="item.label === 'Canciones'" class="w-full mt-40">
              <audio :key="selectedMediaUrl" class="border-2 border-gray-500 w-full" controls>
                <source :src="selectedMediaUrl" type="audio/mp3">
                Your browser does not support the audio tag.
              </audio>
            </div>
          </div>
        </template>
      </UTabs>

    </div>
  </div>
</template>

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