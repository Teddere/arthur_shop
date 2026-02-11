<script setup>
  import {RouterLink} from "vue-router";
</script>

<template>
  <section class="not-found_section">
    <div class="not-found_content">
      <div class="not-found_code">404</div>
      <h1>Page non trouvée</h1>
      <RouterLink :to="'home'" class="btn-not-found">
        <i class="fa-solid fa-home"></i>
        Accueil
      </RouterLink>
    </div>
  </section>
</template>

<style scoped>
.not-found {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, var(--body-color), var(--body-color));
  padding: 20px;
}

.content {
  text-align: center;
  animation: fadeIn 0.6s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.error-code {
  font-size: 120px;
  font-weight: 900;
  color: rgba(var(--primary-rgb), 0.2);
  line-height: 1;
  margin-bottom: 20px;
}

h1 {
  font-size: 32px;
  margin-bottom: 10px;
  color: var(--text-color);
}

p {
  font-size: 16px;
  color: rgba(var(--text-rgb), 0.7);
  margin-bottom: 30px;
}

.btn-home {
  padding: 12px 30px;
  background: rgba(var(--primary-rgb), 1);
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-home:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(var(--primary-rgb), 0.3);
}

@media (max-width: 480px) {
  .error-code {
    font-size: 80px;
  }

  h1 {
    font-size: 24px;
  }

  p {
    font-size: 14px;
  }

  .btn-home {
    padding: 10px 20px;
    font-size: 14px;
  }
}
</style>
