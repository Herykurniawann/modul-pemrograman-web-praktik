$(document).ready(function() {
    $('#btnTambah').click(function() {
       $('#missing-data').hide();
       $.ajax({
        url : 'https://jsonplaceholder.typicode.com/posts',
        type : 'GET',
        dataTyoe : 'json',
        success : function(data) {
            console.log(data);

            $.each(data, function(i, item) {
                let dataRow = `
                    <tr>
                        <td>${item.id}</td>
                        <td>${item.title}</td>
                        <td>${item.body}</td>
                    </tr>
                `
                $('#data').append(dataRow);
            });
        }
        }); 
    })
});