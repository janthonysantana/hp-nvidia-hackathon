<template>
  <div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar -->
    

    <!-- Main content wrapper -->
    <div class="flex-1 flex flex-col">
      <!-- Header -->
      <Header />

      <!-- Page content -->
      <main class="flex-1 overflow-y-auto p-6">
        <div class="max-w-screen-2xl mx-auto space-y-6">
          <slot />
        </div>
      </main>

    </div>
  </div>
</template>

<script setup>
import Sidebar from '@/components/Sidebar.vue'
import Header from '@/components/Header.vue'
</script>
