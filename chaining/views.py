# Create your views here.
from django.http import JsonResponse
from uuid import uuid4
import json

from .utils.blockchain import Blockchain


# Instantiate the Blockchain utility
blockchain = Blockchain()
node_identifier = str(uuid4()).replace('-', '')


def full_chain(request):
    if request.method == "GET":
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
        }
        status_code = 200
    else:
        response = {'message': "inappropriate request"}
        status_code = 400
    return JsonResponse(response, status=status_code)


def mine(request):
    if request.method == "GET":
        last_block = blockchain.last_block
        # We run the proof of work algorithm to get the next proof...
        proof = blockchain.proof_of_work(last_block)

        # We must receive a reward for finding the proof.(amount = 1)
        # The sender is "0" to signify that this node has mined a new coin.
        blockchain.new_transaction(sender="0", recipient=node_identifier, amount=1)

        # Forge the new Block by adding it to the chain
        previous_hash = blockchain.hash(last_block)
        block = blockchain.new_block(proof, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
        }
        status_code = 200
    else:
        response = {'message': "inappropriate request"}
        status_code = 400
    return JsonResponse(response, status=status_code)


def new_transaction(request):
    if request.method == "POST":
        values = request.body

        # Check that the required fields are in the POST'ed data
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return JsonResponse({'message': "Missing values"}, status=400)

        # Create a new Transaction
        index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
        response = {'message': f"Transaction will be added to Block {index}"}
        status_code = 201
    else:
        response = {'message': "inappropriate request"}
        status_code = 400
    return JsonResponse(response, status=status_code)


def register_nodes(request):
    if request.method == "POST":
        # this part needs to be revised
        values = request.body.decode('utf-8')
        values = json.loads(values)
        nodes = values['nodes']
        if nodes is None:
            return JsonResponse({'message': "Error: Please supply a valid list of nodes"}, status=400)

        for node in nodes:
            blockchain.register_node(node)

        response = {
            'message': "New nodes have been added",
            'total_nodes': list(blockchain.nodes)
        }
        status_code = 201
    else:
        response = {'message': "inappropriate request"}
        status_code = 400
    return JsonResponse(response, status=status_code)


def consensus(request):
    if request.method == "GET":
        replaced = blockchain.resolve_conflicts()

        if replaced:  # There is a longest chain on another node
            response = {
                'message': "The chain was replaced",
                'new_chain': blockchain.chain
            }
        else:  # If we've the longest chain among nodes's chains
            response = {
                'message': "The chain is authoritative",
                'chain': blockchain.chain
            }
        status_code = 200
    else:
        response = {'message': "inappropriate request"}
        status_code = 400
    return JsonResponse(response, status=status_code)
