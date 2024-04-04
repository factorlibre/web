# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models
import os

class WebEnvironmentRibbonBackend(models.AbstractModel):

    _name = "web.environment.ribbon.backend"
    _description = "Web Environment Ribbon Backend"

    @api.model
    def _prepare_ribbon(self):
        running_env = os.environ.get("RUNNING_ENV",  "TEST")
        color = os.environ.get("RIBBON_COLOR",  "#f0f0f0")
        bg_color = os.environ.get("RIBBON_BG_COLOR",  "#ff000099")
        storage_name = storage_name.format(env=running_env.upper(), db=self.env.cr.dbname)
        return storage_name, color, bg_color

    @api.model
    def get_environment_ribbon(self):
        """
        This method returns the ribbon data from ir config parameters
        :return: dictionary
        """
        name, color, bg_color = self._prepare_ribbon()
        return {
            "name": name,
            "color": color,
            "background_color": bg_color
        }
