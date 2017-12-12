<div class="form-group row">
	<label class="col-sm-4 col-form-label" for="languages">Languages</label>
	<div class="col-sm-8">	
		<select name="languages" class="form-control" id="languages">
			% for language in languages:
			<option id="lang_{{ language[1] }}" value="{{ language[1] }}"
				% if language[1] == "en":
					selected 
				% end
			>
				{{ language[2] }}
			</option>
			% end
		</select>
	</div>
</div>
