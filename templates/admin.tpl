% include('_header.tpl', title='DJ Parrot - Admin')
<div class="container">
	<div class="row">
		<div class="col-9">
			% include('_nav_bar.tpl')	
			<form method="POST" accept-charset="UTF-8">
				<p align="right">Hi <b>{{ username }}</b>! Once you complete your changes - don't forget to <a href="/logout">logout</a>!</p>
				<input id="admin_action" name="admin_action" type="hidden" value="">
				<div class="form-row">
					<div class="col-3">
						<input id="backup_db" name="backup_db" class="btn btn-info" type="button" value="Create New Backup" onclick="javascript:document.getElementById('admin_action').value='backup';submit();">
					</div>
					<div class="col-2">
						<input id="reset_db" name="reset_db" class="btn btn-secondary" type="button" value="Reset DB" onclick="javascript:document.getElementById('admin_action').value='reset';submit();">
					</div>
					<div class="col-3">
						<input id="restore_db" name="restore_db" class="btn btn-secondary" type="button" value="Restore DB from Backup" onclick="javascript:document.getElementById('admin_action').value='restore';submit();">
					</div>
					<div class="col-4">
						<select id="backups" class="form-control" name="backup">
							% for item in backups:
							<option value="{{ item }}">{{ item.replace("djparrot_", "").replace(".sql", "").replace("_", " ") }}</option>
							% end
						</select>
					</div>
				</div>
				<p>To add custom words, please click <a href="/translate">here</a>.</p>
			</form>
			<hr>
			<div class="row">
				<div class="col">
				% if flashes:
					% for category, message in flashes:
					<div class="alert alert-{{ category }} alert-dismissible" role="alert" width="100%" style="margin-top: 1rem;">
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
