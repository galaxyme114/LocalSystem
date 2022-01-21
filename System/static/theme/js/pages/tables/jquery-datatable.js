$(function () {
    $('.js-basic-example').DataTable({
        responsive: true
    });

    //Exportable table
    $('.js-exportable').DataTable({
        dom: 'Bfrtip',
        responsive: true,
        buttons: [
            'csv', 'excel',
            {
                extend: 'pdfHtml5',
                orientation: 'landscape',
                pageSize: 'LEGAL'
            }
        ],
        "paging":   false,
        "ordering": false,
        "info":     false
    });
});