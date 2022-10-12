$(document).ready(function(e){
    const getTaskURL = 'json';
    $.ajax({
      type: 'GET',
      url: getTaskURL,
      success: function (response) {
        if (!response.length){
          $('#todos-card').prepend(`
          <div class="d-flex justify-content-center" id="no-task-div">
            <h1>No Task</h1>
          </div>`)
        }
        else{
          for (let i = 0; i < response.length; i++){
            addTaskAsync($('#todos-card'), response[i]["fields"], response[i]["pk"]);
          }
        }
      },
      error: function (response) {
          console.log(response)
      }
    })
  });
  
  $("#add-task").click(function(e){
    e.preventDefault();
    const serializedData = getFormData($('#add-task-form'));
    const addTaskURL = 'add/';
    $.ajax({
      type: 'POST',
      url: addTaskURL,
      data: serializedData,
      success: function (response) {
          // on successfull creating object
          $("#add-task-form").trigger('reset');
          $("#title-input").focus();
          // display the newly friend to table.
          var instance = JSON.parse(response);
          var fields = instance[0]["fields"];
          var task_id = instance[0]["pk"];
          if ($('#no-task-div').length){
            $('#no-task-div').remove();
          }
          addTaskAsync($('#todos-card'), fields, task_id);
      },
      error: function (response) {
          // alert the error if any error occured
          alert(response["responseJSON"]["error"]);
      }
    })
    $('#modalCreateTask').modal('hide');
  });
  
  $('#todos-card').ready ( function () {
    $('#todos-card').on('click', '.delete-task-ajax', function(e) {
      e.preventDefault()
      const deleteTaskURL = "delete/" + this.id;
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      $.ajax({
        type: 'DELETE',
        url: deleteTaskURL,
        beforeSend: function (xhr) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      })
      $(`#task-card-${this.id}`).remove();
    });
  });
  
  $('#todos-card').ready ( function () {
    $('#todos-card').on('click', '.update-task-ajax', function(e) {
      e.preventDefault()
      const id = this.id.substring(7);
      const finishTaskURL = "update/" + this.id;
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      $.ajax({
        type: 'POST',
        url: finishTaskURL,
        beforeSend: function (xhr) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      })
      $(`#task-status-${id}`).text("Done");
      $(`#task-status-${id}`).addClass("text-success").removeClass("card-subtitle mb-2 text-danger");
      $(`#${this.id}`).remove();
    });
  });
  
  function getFormData($form){
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};
  
    $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });
  
    return indexed_array;
  }
  
  function addTaskAsync($element, fields, task_id) { 
    const title = fields["title"];
    const description = fields["description"];
    const date = fields["date"];
    const tombol_selesai = (!fields["is_finished"]) ? `<div class="finish-task-ajax" id="finish-${task_id}">` +
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-check-circle text-muted" id="check_task" viewBox="0 0 16 16">' +
        '<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>' +
        '<path d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z"/>' +
    '</svg>' +
  '</div>' : "";
    const status_text = (!fields["is_finished"]) ? `<span class="badge badge-pill badge-warning" id="task-status-${task_id}">In Progress</span>` 
                                                  :  `<span class="badge badge-pill badge-success" id="task-status-${task_id}">Done</span>`
    
    var html = 
    `<div class="container" id="task-card-${task_id}">` +
      `<div class="card" id="card" style="margin-bottom: 20px;">` +

        `<div class="card-header align-middle mb-auto mt-auto">` +
          `<div class="d-flex align-middle pb-2 pt-2">` +
            `<div class="mr-auto p-0 mb-auto mt-auto">` + status_text + `</div>` +
              `<div class="p-1">` + 
                `<h4>Created On: ${date}</h4>` + 
              `</div>` +
            `</div>` +
        `</div>` +
        `<div class="card-body d-flex p-4 pr-2 pl-4">` +
            `<div class="mr-auto justify-content-between" id="desc">`+
              `<h1>${title}<h1><span style="font-size:14px">${description}</span>` +
            `</div>` +
            `<div class="mt-auto align-items-end">` +
              `<button><a href="{% url "todolist:update" todo.id %}", class="update-task-ajax" id="update-${task_id}">Update</a></button>` +
              `<button><a href="{% url "todolist:delete" todo.id %}", class="delete-task-ajax" id="${task_id}">Delete</a></button>`+
            `</div>` +
        '</div>' +
      '</div>' +
    '</div>'
  
    $($element).append(html);
  }