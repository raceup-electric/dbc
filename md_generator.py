import argparse
import cantools

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate Markdown from DBC files.')
    parser.add_argument('--in', dest='inputs', nargs=2, action='append', metavar=('DBC_FILE', 'TITLE'),
                        required=True, help='Input DBC file and its title.')
    parser.add_argument('--out', dest='output', metavar='OUTPUT_FILE', default='output.md',
                        help='Output Markdown file.')
    return parser.parse_args()

def process_dbc_file(dbc_file, title):
    db = cantools.database.load_file(dbc_file)
    content = f"## {title}\n\n"
    index_table = "| Message Name | ID (Dec) | ID (Hex) | Notes |\n|--------------|---------|----------|-------|\n"
    message_details = ""
    
    for message in db.messages:
        notes = message.comment or ""
        index_table += f"| [{message.name}](#{message.name.lower()}) | {message.frame_id} | 0x{message.frame_id:X} | {notes} |\n"
        message_details += f"\n#### {message.name}\n\n"
        message_details += "| ID (Dec) | ID (Hex) | DLC |\n|----------|----------|-----|\n"
        message_details += f"| {message.frame_id} | 0x{message.frame_id:X} | {message.length} |\n\n"
        if message.comment:
            message_details += f"**Comment:** {message.comment}\n\n"
        if message.signals:
            message_details += "| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |\n"
            message_details += "|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|\n"
            for signal in message.signals:
                receivers = ', '.join(signal.receivers)
                message_details += f"| {signal.name} | {signal.start} | {signal.length} | {signal.byte_order} | {signal.is_signed} | {signal.scale} | {signal.offset} | {signal.minimum} | {signal.maximum} | {signal.unit} | {receivers} |\n"
            has_enums = any(signal.choices for signal in message.signals)
            if has_enums:
                message_details += "\n**Enumerations:**\n\n"
                for signal in message.signals:
                    if signal.choices:
                        message_details += f"- **{signal.name}**:\n"
                        for value, description in signal.choices.items():
                            message_details += f"  - {value}: {description}\n"
        message_details += "\n"
    return index_table, message_details

def main():
    args = parse_arguments()
    full_index = ""
    full_content = ""
    for dbc_file, title in args.inputs:
        index_table, message_details = process_dbc_file(dbc_file, title)
        full_index += index_table + "\n"
        full_content += message_details + "\n"
    with open(args.output, 'w') as md_file:
        md_file.write("# DBC Documentation\n\n")
        md_file.write("## Index\n\n")
        md_file.write(full_index)
        md_file.write(full_content)

if __name__ == "__main__":
    main()
