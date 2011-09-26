<%inherit file="base.mako"/>

<%def name="header()">
</%def>

<%def name="body()">

<a class="btn" href="${request.route_url('create-scenario')}">Create new scenario</a>
<h3>Existing Scenarios</h3>

<div class="row">
  <div class="span8">
    <table>      
      <thead>
        <td>Name</td>
        <td>Node count</td>
      </thead>
      <tbody>
        % for scenario in scenarios:        
        <tr>
          <td> 
            <a href="${request.route_url('show-scenario',id=scenario.id)}">${scenario}</a>
          </td>
          <td>
            ${scenario.get_nodes().count()}
          </td>
        </tr>
        % endfor
      </tbody>
    </table>
  </div>
</div>

</%def>
