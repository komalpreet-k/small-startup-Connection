<script setup>
import { ref, onMounted } from "vue";
import BusinessCard from "../components/BusinessCard.vue";

const businesses = ref([]);

onMounted(async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/businesses/");
    const data = await response.json();
    businesses.value = data;
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div>
    <h1>Explore Businesses</h1>

    <BusinessCard
      v-for="business in businesses"
      :key="business.id"
      :business="business"
    />
  </div>
</template>


<style scoped>
.card {
  background: white;
  padding: 20px;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
</style>
