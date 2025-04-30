// Dashboard layout and interaction manager
class DashboardManager {
    constructor() {
        this.metrics = new Map();
        this.layout = null;
        this.gridOptions = {
            cellHeight: 80,
            verticalMargin: 10,
            animate: true,
            float: true,
            removeTimeout: 100,
            disableOneColumnMode: true
        };
    }

    initialize() {
        // Initialize grid layout
        this.layout = new GridStack(this.gridOptions);
        
        // Load saved layout
        this.loadLayout();
        
        // Set up event listeners
        this.setupEventListeners();
        
        // Initialize metrics
        this.initializeMetrics();
    }

    setupEventListeners() {
        // Save layout on change
        this.layout.on('change', () => this.saveLayout());
        
        // Handle window resize
        window.addEventListener('resize', () => this.handleResize());
        
        // Handle metric updates
        document.addEventListener('metricUpdate', (e) => this.handleMetricUpdate(e.detail));
        
        // Handle alert triggers
        document.addEventListener('alertTrigger', (e) => this.handleAlert(e.detail));
    }

    initializeMetrics() {
        // Get all metric elements
        const metricElements = document.querySelectorAll('.metric-card');
        
        metricElements.forEach(element => {
            const metricId = element.dataset.metricId;
            if (metricId) {
                this.metrics.set(metricId, {
                    element,
                    type: element.dataset.metricType,
                    chart: null
                });
                
                // Initialize chart based on metric type
                this.initializeMetricChart(metricId);
            }
        });
    }

    initializeMetricChart(metricId) {
        const metric = this.metrics.get(metricId);
        if (!metric) return;

        const chartElement = metric.element.querySelector('.metric-chart');
        if (!chartElement) return;

        // Get initial data
        const initialData = JSON.parse(metric.element.dataset.initialData || '[]');
        
        // Create appropriate chart based on metric type
        switch (metric.type) {
            case 'gauge':
                metric.chart = createMetricGauge(
                    metricId,
                    chartElement.id,
                    initialData.value,
                    initialData.maxValue
                );
                break;
            case 'line':
            default:
                metric.chart = createMetricChart(
                    metricId,
                    chartElement.id,
                    initialData
                );
                break;
        }
    }

    handleMetricUpdate(update) {
        const metric = this.metrics.get(update.metricId);
        if (!metric) return;

        // Update chart based on metric type
        switch (metric.type) {
            case 'gauge':
                updateMetricGauge(
                    update.metricId,
                    update.value,
                    update.maxValue
                );
                break;
            case 'line':
            default:
                updateMetricChart(update.metricId, {
                    timestamp: update.timestamp,
                    value: update.value
                });
                break;
        }

        // Update metric value display
        const valueElement = metric.element.querySelector('.metric-value');
        if (valueElement) {
            valueElement.textContent = update.value.toFixed(2);
        }
    }

    handleAlert(alert) {
        const metric = this.metrics.get(alert.metricId);
        if (!metric) return;

        // Add alert class to metric card
        metric.element.classList.add('alert-triggered');
        
        // Show alert notification
        this.showAlertNotification(alert);
        
        // Remove alert class after timeout
        setTimeout(() => {
            metric.element.classList.remove('alert-triggered');
        }, 5000);
    }

    showAlertNotification(alert) {
        const notification = document.createElement('div');
        notification.className = 'alert-notification';
        notification.innerHTML = `
            <div class="alert-header">
                <span class="alert-title">${alert.title}</span>
                <button class="close-alert">&times;</button>
            </div>
            <div class="alert-body">
                <p>${alert.message}</p>
                <small>Metric: ${alert.metricName}</small>
            </div>
        `;

        document.body.appendChild(notification);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            notification.remove();
        }, 5000);

        // Handle close button
        notification.querySelector('.close-alert').addEventListener('click', () => {
            notification.remove();
        });
    }

    saveLayout() {
        const layout = this.layout.save();
        localStorage.setItem('dashboardLayout', JSON.stringify(layout));
    }

    loadLayout() {
        const savedLayout = localStorage.getItem('dashboardLayout');
        if (savedLayout) {
            this.layout.load(JSON.parse(savedLayout));
        }
    }

    handleResize() {
        // Update grid layout on window resize
        this.layout.onParentResize();
    }

    addMetric(metricData) {
        // Create metric card element
        const card = document.createElement('div');
        card.className = 'metric-card';
        card.dataset.metricId = metricData.id;
        card.dataset.metricType = metricData.type;
        card.dataset.initialData = JSON.stringify(metricData.initialData);
        
        card.innerHTML = `
            <div class="metric-header">
                <h3>${metricData.name}</h3>
                <div class="metric-actions">
                    <button class="btn-refresh" title="Refresh">
                        <i class="fas fa-sync"></i>
                    </button>
                    <button class="btn-settings" title="Settings">
                        <i class="fas fa-cog"></i>
                    </button>
                </div>
            </div>
            <div class="metric-body">
                <div class="metric-value">${metricData.initialData.value.toFixed(2)}</div>
                <canvas id="chart-${metricData.id}" class="metric-chart"></canvas>
            </div>
        `;

        // Add to grid
        this.layout.addWidget(card);
        
        // Initialize metric
        this.metrics.set(metricData.id, {
            element: card,
            type: metricData.type,
            chart: null
        });
        
        // Initialize chart
        this.initializeMetricChart(metricData.id);
    }

    removeMetric(metricId) {
        const metric = this.metrics.get(metricId);
        if (!metric) return;

        // Remove from grid
        this.layout.removeWidget(metric.element);
        
        // Clean up
        if (metric.chart) {
            chartManager.destroyChart(metricId);
        }
        
        this.metrics.delete(metricId);
    }
}

// Initialize dashboard manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const dashboardManager = new DashboardManager();
    dashboardManager.initialize();
    
    // Export to window for global access
    window.dashboardManager = dashboardManager;
}); 