<template>
  <div class="flex h-screen w-screen overflow-hidden">
    <Sidebar />
      <main class="flex-1 overflow-y-auto overflow-x-hidden bg-gray-100 p-6">
      <DashboardLayout>      
        <!-- Top Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4">
          <DashboardCard title="Current Glucose" value="124 mg/dL" />
          <DashboardCard title="Daily Streaks" value="17 days" />
          <DashboardCard title="Weekly XP" value="1,240 points" />
          <DashboardCard title="Next Insulin" value="2:30 PM" />
        </div>

        <!-- Chart + Daily Missions -->
        <div class="grid grid-cols-1 xl:grid-cols-3 gap-4">
          <!-- Glucose Chart -->
          <GlucoseChart class="xl:col-span-2" />
          
          <!-- Daily Missions -->
          <DailyMissions />
        </div>

        <!-- Bottom Action Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
          <BottomCard
            title="AI Health Coach"
            description="Your personal guide is ready to chat"
            button="Start Conversation"
            color="blue"
          />
          <BottomCard
            title="Food Analysis"
            description="Scan your meals for carb estimation"
            button="Open Scanner"
            color="green"
          />
          <BottomCard
            title="Weekly Report"
            description="Your health summary is ready"
            button="View Report"
            color="orange"
          />
        </div>
      </DashboardLayout>
    </main>
  </div>
</template>

<script setup>
import Sidebar from '@/components/layouts/Sidebar.vue'
import DashboardLayout from '@/components/layouts/DashboardLayout.vue'
import DashboardCard from '@/components/dashboard/DashboardCard.vue'
import GlucoseChart from '@/components/dashboard/GlucoseChart.vue'
import DailyMissions from '@/components/dashboard/DailyMissions.vue'
import BottomCard from '@/components/dashboard/BottomCards.vue'

</script>
