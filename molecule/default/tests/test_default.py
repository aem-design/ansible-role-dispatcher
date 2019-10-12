import os
import testinfra.utils.ansible_runner
import docker


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dispatcher_cached_content_successfully():

    client = docker.client.from_env()
    container = client.containers.get("ansible-role-dispatcher-test")
    exit_code, output = container.exec_run("find /data/httpd/cache/ -name generic-details.html")

    assert '/data/httpd/cache/content/aemdesign-showcase' \
           '/au/en/component/details/generic-details.html' \
           in output.decode("utf-8")

# nothing to test as this role test hosts
