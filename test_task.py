from task import Task


def test_mark_done():
    task = Task("Teisti ülesanne")
    task.mark_done()
    assert task.status == "done"