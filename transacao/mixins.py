from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class New_mixin:
    def create(self, request, *args, **kwargs):

        arq = self.get(request).data
        data = []

        for linha in arq:
        
            json_certo = {}
            json_certo.update({"type": linha["type"]})
            json_certo.update({"date": linha["date"]})
            json_certo.update({"value": float(linha["value"])})
            json_certo.update({"cpf": linha["cpf"]})
            json_certo.update({"card": linha["card"]})
            json_certo.update({"time": linha["time"]})
            json_certo.update({"store_owner": linha["store_owner"]})
            json_certo.update({"store_name": linha["store_name"]})
            data.append(json_certo)


        serializer = self.get_serializer(data=data, many=True)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)