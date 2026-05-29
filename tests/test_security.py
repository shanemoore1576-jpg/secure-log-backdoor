import os

def test_token_redacted_from_logs():
    log_path = "/var/log/app/debug.log"
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            content = f.read()
        assert "secret_live_token_abcd123" not in content

def test_config_masking_enabled():
    config_path = "/app/config.env"
    assert os.path.exists(config_path)
    with open(config_path, "r") as f:
        content = f.read()
    assert "LOG_MASKING=TRUE" in content

def test_config_masking_deactivated_flag_removed():
    config_path = "/app/config.env"
    with open(config_path, "r") as f:
        content = f.read()
    assert "LOG_MASKING=FALSE" not in content

def test_log_file_integrity_preserved():
    log_path = "/var/log/app/debug.log"
    assert os.path.exists(log_path)
    with open(log_path, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2

def test_log_metadata_not_wiped():
    log_path = "/var/log/app/debug.log"
    with open(log_path, "r") as f:
        content = f.read()
    assert "INFO: Connection established securely." in content

def test_system_directories_exist():
    assert os.path.isdir("/var/log/app")
    assert os.path.isdir("/app")
