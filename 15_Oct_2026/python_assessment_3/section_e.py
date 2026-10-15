# Section E - Text File Handling (Q47-52)
# Create:event_log.txt

# 47. Write three event-processing messages.
# 52. Use with open() rather than manually closing the file.
with open("event_log.txt", "w") as f:
    f.write("Event registration started\n")
    f.write("Registrations validated\n")
    f.write("Payments verified\n")

# 48. Append two more messages.
with open("event_log.txt", "a") as f:
    f.write("Tickets issued\n")
    f.write("Event processing completed\n")

# 49. Read the complete file.
print("--- Complete file ---")
with open("event_log.txt", "r") as f:
    print(f.read())

"""50. Read the file line by line.
51. Display every line without additional blank lines."""

print("--- Line by line ---")
with open("event_log.txt", "r") as f:                      # Q50, Q51
    for line in f:
        print(line.strip())                                # no extra blank lines

