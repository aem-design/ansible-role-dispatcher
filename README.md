# Ansible Role: Dispatcher

[![Build Status](https://travis-ci.org/aem-design/ansible-role-dispatcher.svg?branch=master)](https://travis-ci.org/aem-design/ansible-role-dispatcher)

Setup Dispatcher service to go provide cache for your AEM instances.
> This role was developed as part of
> [AEM.Design](http://aem.design/)

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

| Name                         	| Required 	| Default                                                   	| Notes                                                                	|
|------------------------------	|----------	|-----------------------------------------------------------	|----------------------------------------------------------------------	|
| docker_image_user            	|          	| aemdesign                                                 	|                                                                      	|
| docker_image_name            	|          	| dispatcher                                                	|                                                                      	|
| docker_image                 	|          	| {{ docker_image_user }}/{{ docker_image_name }}           	|                                                                      	|
| docker_image_tag             	|          	| latest                                                    	|                                                                      	|
| docker_container_name        	|          	| author-dispatcher                                         	|                                                                      	|
|                              	|          	|                                                           	|                                                                      	|
| docker_container_user        	|          	| apache                                                    	|                                                                      	|
| docker_container_userid      	|          	| 1100                                                      	|                                                                      	|
| docker_container_group       	|          	| {{ docker_container_user }}                               	|                                                                      	|
| docker_container_groupid     	|          	| 1100                                                      	|                                                                      	|
|                              	|          	|                                                           	|                                                                      	|
|                              	|          	|                                                           	|                                                                      	|
| apache_modules               	|          	| /dispatcher/httpd/modules                                 	|                                                                      	|
| apache_ssl_subj              	|          	| /c=au/st=vic/l=melbourne/o=aem design/cn=dispatcher       	|                                                                      	|
| apache_run_user              	|          	| apache                                                    	|                                                                      	|
| apache_run_group             	|          	| apache                                                    	|                                                                      	|
| apache_run_userid            	|          	| 1100                                                      	|                                                                      	|
| apache_run_groupid           	|          	| 1100                                                      	|                                                                      	|
| apache_loglevel              	|          	| info                                                      	|                                                                      	|
| apache_version               	|          	| 2.4                                                       	|                                                                      	|
| dispatcher_version           	|          	| 4.3.2                                                     	|                                                                      	|
| dispatcher_loglevel          	|          	| 2                                                         	| log level for the dispatcher module: error, warn, info, debug, trace 	|
| dispatcher_config            	|          	| author                                                    	|                                                                      	|
| dispatcher_name              	|          	| dispatcher                                                	|                                                                      	|
| dispatcher_propogatesyndpost 	|          	| 0                                                         	|                                                                      	|
| dispatcher_servestaleonerror 	|          	| 1                                                         	|                                                                      	|
| dispatcher_statlevel         	|          	| 3                                                         	|                                                                      	|
| dispatcher_cacheauthorized   	|          	| 0                                                         	|                                                                      	|
| dispatcher_sessionmanagement 	|          	| 0                                                         	|                                                                      	|
| renderer_host                	|          	| localhosy                                              	|                                                                      	|
| renderer_port                	|          	| 4502                                                      	|                                                                      	|
| renderer_timeout             	|          	| 10000                                                     	|                                                                      	|
| renderer_resolve             	|          	| 1                                                         	|                                                                      	|
| dispatcher_port              	|          	| {{ service_dispatcher_port | default('80') }}             	|                                                                      	|
| dispatcher_https_port        	|          	| {{ service_dispatcher_https_port | default('443') }}      	|                                                                      	|
|                              	|          	|                                                           	|                                                                      	|
| docker_published_ports       	|          	|                                                           	|                                                                      	|
|                              	|          	| "0.0.0.0:{{ dispatcher_port }}:8080/tcp",                 	|                                                                      	|
|                              	|          	| "0.0.0.0:{{ dispatcher_https_port }}:8443/tcp"            	|                                                                      	|
|                              	|          	|                                                           	|                                                                      	|
| docker_volumes               	|          	|                                                           	|                                                                      	|
|                              	|          	| "author-dispatcher-cache:/data/httpd/cache:z",            	|                                                                      	|
|                              	|          	| "author-dispatcher-logs:/data/httpd/logs:z"               	|                                                                      	|
|                              	|          	|                                                           	|                                                                      	|
| iptable_rules                	|          	|                                                           	|                                                                      	|
|                              	|          	| - port: "{{ aem_port | default('80') }}"                  	|                                                                      	|
|                              	|          	| comment: "service_{{ docker_container_name }}_port"       	|                                                                      	|
|                              	|          	| - port: "{{ aem_debug_port | default('443') }}"           	|                                                                      	|
|                              	|          	| comment: "service_{{ docker_container_name }}_debug_port" 	|                                                                      	|


## Dependencies

This role depends on role `aem_design.docker_container`.

## Example Playbook

```yaml
  - hosts: all
    roles:
      - {
        role: dispatcher,
        renderer_port: "{{ service_author_port | default('4502') }}",
        renderer_host: "{{ service_aem_host | default('localhost') }}",
        dispatcher_port: "{{ service_dispatcher_author_port | default('81') }}",
        dispatcher_https_port: "{{ service_dispatcher_author_https_port | default('444') }}",
        dispatcher_version: "{{ service_dispatcher_image_tag | default('4.3.2') }}",
        docker_container_name: "author-dispatcher",
        docker_volumes: [
          "author-dispatcher-cache:/data/httpd/cache:z",
          "author-dispatcher-logs:/data/httpd/logs:z"
          ],
        docker_published_ports: [
          "0.0.0.0:{{ service_dispatcher_author_port }}:8080/tcp",
          "0.0.0.0:{{ service_dispatcher_author_https_port }}:8443/tcp"
          ],
        tags: dispatcher-author
      }
```

## License

Apache 2.0

## Author Information

This role was created by [Max Barrass](https://aem.design/).