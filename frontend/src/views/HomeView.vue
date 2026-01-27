<script setup>
import { ref, onMounted } from "vue";
import BusinessCard from "../components/BusinessCard.vue";

const businesses = ref([]);
const categories = ref([]);
const countries = ref([]);

const selectedCategory = ref("");
const selectedCountry = ref("");

const fetchBusinesses = async () => {
  let url = "http://127.0.0.1:8000/api/businesses/";

  const params = [];

  if (selectedCategory.value) {
    params.push(`category=${selectedCategory.value}`);
  }

  if (selectedCountry.value) {
    params.push(`country=${selectedCountry.value}`);
  }

  if (params.length > 0) {
    url += "?" + params.join("&");
  }

  const response = await fetch(url);
  businesses.value = await response.json();
};

const fetchCategories = async () => {
  const response = await fetch("http://127.0.0.1:8000/api/categories/");
  categories.value = await response.json();
};

const fetchCountries = async () => {
  const response = await fetch("http://127.0.0.1:8000/api/countries/");
  countries.value = await response.json();
};

onMounted(async () => {
  await fetchCategories();
  await fetchCountries();
  await fetchBusinesses();
});
</script>


<template>
  <div>
    <h1>Explore Businesses</h1>

    <div class="filters">
      <select v-model="selectedCategory" @change="fetchBusinesses">
        <option value="">All Categories</option>
        <option v-for="cat in categories" :key="cat.id" :value="cat.id">
          {{ cat.name }}
        </option>
      </select>

      <select v-model="selectedCountry" @change="fetchBusinesses">
        <option value="">All Countries</option>
        <option v-for="country in countries" :key="country.id" :value="country.id">
          {{ country.name }}
        </option>
      </select>
    </div>

    <BusinessCard
      v-for="business in businesses"
      :key="business.id"
      :business="business"
    />
  </div>
</template>



<style scoped>
.filters {
  margin-bottom: 20px;
  display: flex;
  gap: 15px;
}

select {
  padding: 8px;
  border-radius: 6px;
  border: 1px solid #ccc;
}
</style>

