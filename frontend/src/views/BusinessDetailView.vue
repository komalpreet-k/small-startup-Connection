<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const business = ref(null);

onMounted(async () => {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/businesses/${route.params.id}/`
    );
    business.value = await response.json();
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div v-if="!business">Loading...</div>

  <div v-else>
    <h1>{{ business.name }}</h1>
    <p><strong>Category:</strong> {{ business.category.name }}</p>
    <p><strong>Location:</strong> {{ business.city.name }}, {{ business.state.name }}</p>
    <p><strong>Instagram:</strong> {{ business.instagram_url }}</p>
    <hr />
    <p>{{ business.description }}</p>
  </div>
</template>
