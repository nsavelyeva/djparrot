% include('_header.tpl', title='DJ Parrot - Search')
<div class="container">
	<div class="row">
		<div class="col-9">
			% include('_nav_bar.tpl')	
			<form method="POST" accept-charset="UTF-8">
				% include('_h_languages.tpl')
				<div class="form-row">
					<div class="col-6">
						<input id="search" name="search" class="form-control" type="text" value="{{ entry }}">
					</div>
					<div class="col-4">
						<input id="submit" name="submit" class="btn btn-secondary" type="submit" value="Collect words" style="width: 100%">
					</div>
				</div>
			</form>
			<hr>
			<div class="row">
				<div class="col">
				% if flashes:
					% for category, message in flashes:
					<div class="alert alert-{{ category }} alert-dismissible" role="alert" width="100%">
						<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
						<strong>{{ category.title() }}!</strong> {{ message }}
					</div>
					% end
				% end
				</div>
			</div>
			<div class="form-row">
				<div class="col-8">
					<div id="result"></div>
					% if words:
					<table id="words" class="table table-bordered table-hover table-sm">
						<thead class="thead-light"><tr id="table_headers"><th>#</th>
						% for item in lang_checkbox:
							<th>{{ item }}</th>
						% end
						<th>Exclude</th></tr></thead>
						<tbody id="table_body">
						%for i in range(0, len(words)):
						<tr><th>{{ i+1 }}</th>
							% for item in lang_checkbox:
							<td id="{{ item }}_{{ i+1 }}">{{! words[i][item] }}&nbsp;<i name="say_word" class="fa fa-volume-up" aria-hidden="true"></i></td>
							% end
						<td><i name="del_row" class="fa fa-trash" aria-hidden="true"></i></td></tr>
						% end
						</tbody>
					</table>
					% end
				</div>
			</div>

			<hr>
			<p id="statistics"></p>

		</div>
		<div class="col">
			% include('_buttons.tpl')
			% include('_controls.tpl')
		</div>
	</div>
</div>

% include('_footer.tpl')
