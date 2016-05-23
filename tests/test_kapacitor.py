
def test_kapacitor_running_and_enabled(Service):
    kapacitor = Service("kapacitor")
    assert kapacitor.is_running
    assert kapacitor.is_enabled

def test_kapacitor_config(File):
    kapacitor_config = File("/etc/kapacitor/kapacitor.conf")
    assert kapacitor_config.exists
    assert 'test_db = ["rp_test_db"]' in kapacitor_config.content_string
    assert 'test_db_2 = ["rp_test_db_one", "rp_test_db_two"]' in kapacitor_config.content_string

def test_tick_file(File):
    tick_script = File("/tmp/cpu_alert.tick")
    assert tick_script.exists

def test_tick_load(Command):
    tick_load = Command("kapacitor list tasks")
    assert "cpu_alert" in tick_load.stdout
