
$(document).ready(function () {            
      
   $('.unit').change(function(){
        if($(this).val()!=''){
        var select=$(this).val();
        var _token=$('input[name="_token"]').val();
        $.ajax({
                url:"{{route('fectunit')}}",
                method:"GET",
                data:{select:select,_token:_token},
                success:function(result){
                   $('.unitsub').html(result);
                }
        })
       // console.log(select);
        }        
   });

    //Add Modal Data Unitsub
   $('.adddataunit').on('submit', function(e){
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: 'articles_unitsub_save',
            data:$('.adddataunit').serialize(),
            success:function(result){
                console.log(result);
                $('.addModal').modal('hide');               
                location.reload();
            },
            error:function(error){
                console.log(error);
               
            }
        });
   });

   var table = $('#dataTable').dataTable();

   //Edit Modal Data Unitsub
//    table.on('click','.edit',function(){
//        $tr = $(this).closest('tr');
//        if ($($tr).hasClass('child')) {
//            $tr = $tr.prev('.parent');
//        }

//        var data = table.row($tr).data();
//        console.log(data);

//        $('#unit_name').val(data[1]);
//        $('#unitsub_qty').val(data[2]);
//        $('#unitsub_name').val(data[3]);

//        $('#editForm').attr('action', 'articles_unitsub_update/'+data[0]);
//        $('#editModal').modal('show');

//    });


});
