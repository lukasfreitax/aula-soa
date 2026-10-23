from flask import Blueprint, request, jsonify
from service.veiculo_service import VeiculoService
from model.veiculo import Veiculo

veiculo_bp = Blueprint("veiculo", __name__)

service = VeiculoService()

@veiculo_bp.route("/veiculo", methods=["GET","POST"])
def veiculo():
    if request.method == "POST":
        json = request.json
        veiculo = Veiculo(**json)
        service.cadastrar(veiculo)
        return jsonify({"mensagem":"Veículo cadastrado!"})
    veiculos = service.listar()
    return jsonify([veiculo.to_dict() for veiculo in veiculos])
    