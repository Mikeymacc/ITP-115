from lxml import etree

def computetotal(no, file='orders.xml'):
    tree = etree.parse(file)
    root = tree.getroot()
    xpath = f"/orders/order[@no='{no}']/entry/quantity"
    elements = root.xpath(xpath)
    total = 0
    for quantity in elements:
        total += int(quantity.text)
    return total


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("No order number included")
        sys.exit(1)
    no = sys.argv[1]
    total = computetotal(no)
    print(f"Total number of products in order {no}: {total}")

