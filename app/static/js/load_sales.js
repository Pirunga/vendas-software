let currentPage = 1;
let isLoading = false;

async function loadSales() {
    if (isLoading) return;
    isLoading = true;

    try {
        console.log(`Loading page ${currentPage}...`);
        
        const response = await fetch(`/get_sales?page=${currentPage}`);
        
        if (!response.ok) {
            console.error("Erro ao carregar os dados:", response.statusText);
            return;
        }

        const data = await response.json();
        console.log("Dados recebidos:", data);

        const salesTableBody = document.getElementById('sales-table-body');

        data.sales.forEach(sale => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${sale.date}</td>
                <td>${sale.customer_name}</td>
                <td>${sale.product}</td>
                <td>${sale.quantity}</td>
                <td>${sale.unit_price}</td>
                <td>${sale.total_sale}</td>
            `;
            salesTableBody.appendChild(row);
        });

        isLoading = false;
        currentPage += 1;
        document.getElementById('loading-message').style.display = data.has_next ? 'block' : 'none';

    } catch (error) {
        console.error("Erro na solicitação:", error);
        isLoading = false;
    }
}

window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
        loadSales();
    }
});

loadSales();
