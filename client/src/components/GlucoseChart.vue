<template>
  <div class="bg-white p-6 rounded-xl shadow h-full">
    <h2 class="text-lg font-semibold mb-4 text-gray-700">Glucose Trends</h2>
    <LineChart :chart-data="chartData" :chart-options="chartOptions" />
  </div>
</template>

<script setup>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale
} from 'chart.js'
import { Line as LineChart } from 'vue-chartjs'

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale)

const chartData = {
  labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  datasets: [
    {
      label: 'Glucose Level (mg/dL)',
      data: [110, 125, 140, 130, 120, 135, 128],
      borderColor: '#3b82f6',
      backgroundColor: 'rgba(59, 130, 246, 0.2)',
      fill: true,
      tension: 0.4,
    },
  ],
}

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
      suggestedMax: 180,
    },
  },
}
</script>

<style scoped>
div {
  height: 300px;
}
</style>
