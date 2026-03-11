try:
    result = risky_operation()
except ValueError as e:
    # runs ONLY if ValueError is raised
    print(f"Bad value: {e}")
except (TypeError, KeyError) as e:
    # catch multiple exception types
    print(f"Type or key error: {e}")
except Exception as e:
    # catch-all - use sparingly, always log
    print(f"Unexpected: {e}")
    raise # re-raise so you don't hide bugs
else:
    save(result)
finally:
    cleanup_resources()
