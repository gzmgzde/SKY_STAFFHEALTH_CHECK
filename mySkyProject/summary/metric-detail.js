// metric-detail.js

// Example data for each metric
const metricData = {
  EASY_TO_RELEASE: {
    title: 'Easy to release',
    question: 'Is releasing simple, safe, painless and mostly automated?',
    comments: `Releases have become more challenging recently, with some manual steps and last-minute changes adding complexity. While past improvements in automation and rollback strategies have helped, there are still concerns about reliability and safeguards. Clever documentation, more automation, and structured pre-release checks would help make the process smoother and more predictable.`,
    summary: `<p class="alert">PERFORMANCE DECLINING!</p><p>The team's declining progression in the release process in Q1 2024 reveals growing complexity, with recent releases becoming more challenging due to manual steps and last-minute changes. Despite earlier gains in automation and rollback strategies, concerns about reliability and safeguards persist.</p><p>To reverse this trend, the team should focus on improving documentation, increasing automation, and implementing structured pre-release checks to create a simpler, safer, and more predictable process.</p>`,
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [2, 5, 4, 3],
      backgroundColor: ['#F44336', '#4CAF50', '#4CAF50', '#FFC107']
    }
  },
  DELIVERING_VALUE: {
    title: 'Delivering Value',
    question: 'Are we delivering value to our customers regularly?',
    comments: 'The team has maintained a steady pace in delivering value, but there is room for improvement in prioritizing impactful features.',
    summary: '<p>Delivery cadence is stable, but focus on high-impact work and customer feedback can further boost value.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [3, 4, 4, 3],
      backgroundColor: ['#FFC107', '#4CAF50', '#4CAF50', '#FFC107']
    }
  },
  HEALTH_OF_CODEBASE: {
    title: 'Health of Codebase',
    question: 'Is our codebase healthy, maintainable, and well-tested?',
    comments: 'Code quality has improved with better reviews and refactoring, but technical debt remains in some modules.',
    summary: '<p>Continue refactoring and increase test coverage to maintain code health.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [3, 4, 5, 4],
      backgroundColor: ['#FFC107', '#4CAF50', '#4CAF50', '#4CAF50']
    }
  },
  LEARNING: {
    title: 'Learning',
    question: 'Are we learning and improving as a team?',
    comments: 'Regular knowledge sharing and upskilling sessions have boosted team learning.',
    summary: '<p>Maintain momentum with more cross-team learning opportunities.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [4, 4, 5, 4],
      backgroundColor: ['#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50']
    }
  },
  FUN: {
    title: 'Fun',
    question: 'Are we having fun and enjoying our work?',
    comments: 'Team events and a positive atmosphere have kept morale high.',
    summary: '<p>Keep up the fun activities and celebrate wins together.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [4, 5, 5, 4],
      backgroundColor: ['#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50']
    }
  },
  MISSION: {
    title: 'Mission',
    question: 'Is our mission clear and motivating?',
    comments: 'Mission is clear, but regular reminders and alignment sessions help.',
    summary: '<p>Reinforce mission alignment in team meetings.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [3, 4, 4, 3],
      backgroundColor: ['#FFC107', '#4CAF50', '#4CAF50', '#FFC107']
    }
  },
  PAWNS_OR_PLAYERS: {
    title: 'Pawns or Players',
    question: 'Do we feel empowered to make decisions and contribute?',
    comments: 'Some team members feel less empowered; more autonomy is needed.',
    summary: '<p class="alert">PERFORMANCE DECLINING!</p><p>Increase empowerment and involve everyone in decision-making.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [2, 3, 3, 2],
      backgroundColor: ['#F44336', '#FFC107', '#FFC107', '#F44336']
    }
  },
  SUITABLE_PROCESS: {
    title: 'Suitable Process',
    question: 'Are our processes suitable and efficient?',
    comments: 'Processes are mostly suitable, but some steps could be streamlined.',
    summary: '<p>Review and optimize processes for efficiency.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [3, 4, 4, 3],
      backgroundColor: ['#FFC107', '#4CAF50', '#4CAF50', '#FFC107']
    }
  },
  SPEED: {
    title: 'Speed',
    question: 'Are we delivering at a good pace?',
    comments: 'Delivery speed is good, but bottlenecks occasionally occur.',
    summary: '<p>Identify and address bottlenecks to maintain speed.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [3, 4, 4, 3],
      backgroundColor: ['#FFC107', '#4CAF50', '#4CAF50', '#FFC107']
    }
  },
  SUPPORT: {
    title: 'Support',
    question: 'Do we feel supported by our team and leadership?',
    comments: 'Support from team and leadership is strong.',
    summary: '<p>Continue fostering a supportive environment.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [4, 5, 5, 4],
      backgroundColor: ['#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50']
    }
  },
  TEAMWORK: {
    title: 'Teamwork',
    question: 'Are we collaborating effectively as a team?',
    comments: 'Teamwork is strong, with good collaboration and communication.',
    summary: '<p>Maintain open communication and collaboration.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [4, 5, 5, 4],
      backgroundColor: ['#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50']
    }
  },
  WORK_LIFE: {
    title: 'Work-Life',
    question: 'Is our work-life balance healthy?',
    comments: 'Work-life balance is good, with flexibility and support.',
    summary: '<p>Continue supporting flexible work arrangements.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [4, 5, 5, 4],
      backgroundColor: ['#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50']
    }
  },
  RIGHT_TOOLS: {
    title: 'Right Tools',
    question: 'Do we have the right tools to do our job?',
    comments: 'The team has access to the right tools and resources.',
    summary: '<p>Keep tools up to date and provide training as needed.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [4, 5, 5, 4],
      backgroundColor: ['#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50']
    }
  },
  TESTING: {
    title: 'Testing',
    question: 'Is our testing process effective and reliable?',
    comments: 'Testing is improving, but more automation is needed.',
    summary: '<p>Increase test automation and coverage.</p>',
    chart: {
      labels: ['2023 - Q1', '2023 - Q2', '2023 - Q3', '2024 - Q1'],
      data: [3, 4, 4, 3],
      backgroundColor: ['#FFC107', '#4CAF50', '#4CAF50', '#FFC107']
    }
  }
};

// Get metric from URL
function getMetricKey() {
  const params = new URLSearchParams(window.location.search);
  return params.get('metric');
}

function renderMetricDetail() {
  const metricKey = getMetricKey();
  const data = metricData[metricKey];
  
  if (!data) {
    console.log('No data found for metric: ' + metricKey);
    return;
  }
  
  // Update breadcrumb
  document.getElementById('metricBreadcrumb').textContent = metricKey.replace(/_/g, ' ');
  
  // Update content
  document.getElementById('metricTitle').textContent = data.title;
  document.getElementById('metricQuestion').textContent = data.question;
  document.getElementById('metricComments').textContent = data.comments;
  document.getElementById('metricSummary').innerHTML = data.summary;
  
  // Position marker based on data values
  const marker = document.querySelector('.scale-marker');
  const lastValue = data.chart.data[data.chart.data.length - 1];
  
  if (lastValue <= 2) {
    marker.style.left = '20%';
  } else if (lastValue <= 3) {
    marker.style.left = '50%';
  } else {
    marker.style.left = '80%';
  }

  // Render chart
  const ctx = document.getElementById('progressionChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: data.chart.labels,
      datasets: [{
        label: data.title,
        data: data.chart.data,
        backgroundColor: data.chart.backgroundColor,
        borderRadius: 8
      }]
    },
    options: {
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          beginAtZero: true,
          min: 0,
          max: 5,
          ticks: { stepSize: 1 }
        }
      }
    }
  });
}

document.addEventListener('DOMContentLoaded', renderMetricDetail); 