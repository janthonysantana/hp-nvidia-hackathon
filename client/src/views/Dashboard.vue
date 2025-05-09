<template>
  <DashboardLayout>
    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4 p-4">
      <DashboardCard title="Current Glucose" value="124 mg/dL" />
      <DashboardCard title="Daily Streaks" value="17 days" />
      <DashboardCard title="Weekly XP" value="1,240 points" />
      <DashboardCard title="Next Insulin" value="2:30 PM" />
    </div>

    <!-- Add your chart and Daily Missions here -->
  </DashboardLayout>
</template>

<script setup>
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import DashboardCard from '@/components/DashboardCard.vue'
</script>
