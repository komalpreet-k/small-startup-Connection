<script setup>
import { ref, onMounted } from "vue";
import BusinessCard from "../components/BusinessCard.vue";

const businesses = ref([]);
const categories = ref([]);
const countries = ref([]);
const states = ref([]);

const selectedCategory = ref("");
const selectedCountry = ref("");
const selectedState = ref("");

// Fetch businesses with all filters applied
const fetchBusinesses = async () => {
  let url = "http://127.0.0.1:8000/api/businesses/";

  const params = [];

  if (selectedCategory.value) {
    params.push(`category=${selectedCategory.value}`);
  }

  if (selectedCountry.value) {
    params.push(`country=${selectedCountry.value}`);
  }

  if (selectedState.value) {
    params.push(`state=${selectedState.value}`);
  }

  if (params.length > 0) {
    url += "?" + params.join("&");
  }

  const response = await fetch(url);
  businesses.value = await response.json();
};

// Fetch categories
const fetchCategories = async () => {
  const response = await fetch("http://127.0.0.1:8000/api/categories/");
  categories.value = await response.json();
};

// Fetch countries
const fetchCountries = async () => {
  const response = await fetch("http://127.0.0.1:8000/api/countries/");
  countries.value = await response.json();
};

// Fetch states based on selected country
const fetchStates = async () => {
  if (!selectedCountry.value) {
    states.value = [];
    return;
  }

  const response = await fetch(
    `http://127.0.0.1:8000/api/states/?country=${selectedCountry.value}`
  );
  states.value = await response.json();
};

// When country changes
const handleCountryChange = async () => {
  selectedState.value = "";
  await fetchStates();
  await fetchBusinesses();
};

// When state changes
const handleStateChange = async () => {
  await fetchBusinesses();
};

// When category changes
const handleCategoryChange = async () => {
  await fetchBusinesses();
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
      <!-- Category -->
      <select v-model="selectedCategory" @change="handleCategoryChange">
        <option value="">All Categories</option>
        <option v-for="cat in categories" :key="cat.id" :value="cat.id">
          {{ cat.name }}
        </option>
      </select>

      <!-- Country -->
      <select v-model="selectedCountry" @change="handleCountryChange">
        <option value="">All Countries</option>
        <option v-for="country in countries" :key="country.id" :value="country.id">
          {{ country.name }}
        </option>
      </select>

      <!-- State -->
      <select
        v-model="selectedState"
        @change="handleStateChange"
        :disabled="!selectedCountry"
      >
        <option value="">All States</option>
        <option v-for="state in states" :key="state.id" :value="state.id">
          {{ state.name }}
        </option>
      </select>
    </div>

    <div v-if="businesses.length === 0">
      No businesses found.
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

h1 {
  margin-bottom: 20px;
}
</style>
