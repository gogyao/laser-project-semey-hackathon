function paginateTable(tableId, paginationId, rowsPerPage = 5) {
    const table = document.getElementById(tableId);
    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));
    const totalPages = Math.ceil(rows.length / rowsPerPage);

    function showPage(page) {
        rows.forEach(row => row.style.display = "none");
        const start = (page - 1) * rowsPerPage;
        const end = start + rowsPerPage;
        rows.slice(start, end).forEach(row => row.style.display = "");
        renderPagination(page);
    }

    function renderPagination(currentPage) {
        const pagination = document.getElementById(paginationId);
        pagination.innerHTML = "";

        for (let i = 1; i <= totalPages; i++) {
            const btn = document.createElement("button");
            btn.innerText = i;
            btn.style.margin = "0 5px";
            if (i === currentPage) btn.disabled = true;

            btn.addEventListener("click", () => showPage(i));
            pagination.appendChild(btn);
        }
    }

    showPage(1);
}

document.addEventListener("DOMContentLoaded", () => {
    paginateTable("fields", "pagination-fields");
    paginateTable("operations", "pagination-operations");
    paginateTable("devices", "pagination-devices");
});