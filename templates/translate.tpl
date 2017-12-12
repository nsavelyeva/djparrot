% include('_header.tpl', title='DJ Parrot - Translate')
<div class="container">
	<div class="row">
		<div class="col-9">
			% include('_nav_bar.tpl')
			<form method="POST" accept-charset="UTF-8">
				<p align="right">Dear <b>{{ username }}</b>! Once you complete your changes - don't forget to <a href="/logout">logout</a>!</p>
				<div class="form-row">
					<div class="col-4">
						<select id="src_language" class="form-control" name="src_language">
						% for item in languages:
							<option value="{{ item[1] }}"
							% if item[1] == src_language:
								selected 
							% end
						>{{ item[2] }}</option>
						% end
						</select>
					</div>
					<div class="col-6">
						<input id="entry" name="entry" class="form-control" type="text" value="{{ entry }}">
					</div>
					<div class="col-2">
						<input id="submit" name="submit" class="btn btn-secondary" type="submit" value="Translate">
					</div>
				</div>
				<p>To backup/restore/reset the database, please click <a href="/admin">here</a>.</p>
			</form>
			<hr>
			<div class="form-row">
				<div class="col-9">
					<div id="result"></div>
					% if translation:
					<table id="words" class="table table-bordered table-hover table-sm">
						<thead class="thead-light"><tr id="table_headers">
							<th>Language</th><th>Translation</th><th style="visibility:hidden"></th>
						</thead>
						<tbody id="table_body">
							% for item in languages:
							<tr>
								<th>{{ item[2] }}</th>
								<td id="{{ item[1] }}_read">{{! translation[item[1]] }}&nbsp;<i name="say_word" class="fa fa-volume-up" aria-hidden="true"></i></td>
								<td id="{{ item[1] }}_value" style="visibility:hidden">{{! translation[item[1]] }}</td>
							</tr>
							% end
						</tbody>
					</table>
					<hr>
					<p>Would you like to add translations to the database?<br>Select a category and click on 'Confirm'!</p>
					<div class="form-row">
						<div class="col-5">
							<select id="subcategory" class="form-control" name="subcategory">
							% for item in subcategories:
								<option value="{{ item[0] }}">{{ item[2] }}</option>
							% end
							</select>
						</div>
						<div class="col-4">
							<button id="add_to_db" type="button" class="btn btn-info" title="Add word to Database">Confirm</button>&nbsp;
						</div>
					</div>
					% end
				</div>
			</div>

			<div class="row" style="margin-top:.5em">
				<div id="flashes" class="col-8">
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
